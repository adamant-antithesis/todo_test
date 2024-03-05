from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from .models import Task


class TaskListViewTest(TestCase):
    """Test case for the TaskListView."""
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

        for i in range(30):
            Task.objects.create(title=f'Task {i}', description=f'Description {i}', status='In Progress')

        self.client = Client()

    def test_task_list_view(self):
        """Test the TaskListView."""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['page_obj'].object_list), 20)


class TaskDetailViewTest(TestCase):
    """Test case for the TaskDetailView."""
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Task.objects.create(title='Test Task', description='Test Description', status='In Progress')
        self.client = Client()

    def test_task_detail_view(self):
        """Test the TaskDetailView."""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('task_detail', kwargs={'task_id': self.task.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['task'].title, 'Test Task')
        self.assertEqual(response.context['task'].description, 'Test Description')
        self.assertEqual(response.context['task'].status, 'In Progress')

    def test_task_status_editing(self):
        """Test editing task status."""
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('task_detail', args=[self.task.id]),
                                    {'status': 'In Review', 'assigned_to': self.user.id})
        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.status, 'In Review')
        self.assertEqual(updated_task.assigned_to, self.user)

    def test_task_title_description_editing(self):
        """Test editing task title and description."""
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('task_detail', args=[self.task.id]),
                                    {'title': 'Updated Task Title', 'description': 'Updated Task Description'})
        updated_task = Task.objects.get(id=self.task.id)
        self.assertEqual(updated_task.title, 'Updated Task Title')
        self.assertEqual(updated_task.description, 'Updated Task Description')

    def test_task_deletion(self):
        """Test deleting a task."""
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('task_detail', args=[1]), {'delete_task': True}, follow=True)
        self.assertRedirects(response, reverse('task_list'))


class TaskModelTest(TestCase):
    """Test case for the Task model."""
    @classmethod
    def setUp(cls):
        cls.test_user = User.objects.create_user(username='testuser', password='12345')
        cls.test_task = Task.objects.create(title='Test Task',
                                            description='Test Description',
                                            status=Task.Status.OPEN,
                                            assigned_to=cls.test_user)

    def test_title_max_length(self):
        """Test maximum length of the title field."""
        task = Task.objects.get(id=self.test_task.id)
        max_length = task._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_assigned_user(self):
        """Test the assigned user method."""
        task = Task.objects.get(id=self.test_task.id)
        self.assertEqual(task.assigned_user(), 'testuser')

    def test_default_status(self):
        """Test the default status of the task."""
        task = Task.objects.get(id=self.test_task.id)
        self.assertEqual(task.status, Task.Status.OPEN)

    def test_str_representation(self):
        """Test the string representation of the task."""
        task = Task.objects.get(id=self.test_task.id)
        self.assertEqual(str(task), 'Test Task')
