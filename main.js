const todoList = document.querySelector('#todo-list');
const taskInput = document.querySelector('#task');
const dueDateInput = document.querySelector('#due_date');

todoList.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData(event.target);
  fetch('/create_todo', {
    method: 'POST',
    body: formData
  })
  .then(response => response.redirected ? window.location.replace(response.url) : response.text())
  .then(task => {
    const todoList = document.querySelector('#todo-list');
    const newTask = document.createElement('li');
    newTask.textContent = task.title + (task.due_date ? ' (due ' + task.due_date + ')' : '');
    todoList.appendChild(newTask);
    taskInput.value = '';
    dueDateInput.value = '';
  })
  .catch(error => console.error(error));
});
