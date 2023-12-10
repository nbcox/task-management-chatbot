# Basic Task Chatbot
# Author: Nick Cox
# Date: 2023-12-10


class TaskChatbot:
    def __init__(self):
        self.tasks = []

    def start_chat(self):
        print("Welcome to the Task Chatbot!")
        print(
            "You can create, assign, mark as complete, delete, and discuss tasks. Type 'exit' to end the chat.\n"
        )

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("\nExiting Task Chatbot. Goodbye!")
                break
            else:
                self.process_user_input(user_input)

    def process_user_input(self, user_input):
        user_input = user_input.lower()
        # Basic command recognition for demonstration
        if "create task" in user_input:
            task_name = user_input.split("create task ")[-1]
            self.create_task(task_name)
        elif "assign" in user_input:
            task_index, assignee = map(
                str.strip, user_input.split("assign ")[-1].split(" to ")
            )
            self.assign_task(task_index, assignee)
        elif "mark as complete" in user_input:
            task_index = int(user_input.split("mark as complete ")[-1]) - 1
            self.mark_task_complete(task_index)
        elif "delete task" in user_input:
            task_index = int(user_input.split("delete task ")[-1]) - 1
            self.delete_task(task_index)
        elif "show tasks" in user_input:
            self.show_tasks()
        else:
            print(
                "Chatbot: I'm sorry, I didn't understand that. Please try another command."
            )

    def create_task(self, task_name):
        new_task = {"name": task_name, "status": "To Do"}
        self.tasks.append(new_task)
        print(f"Chatbot: Task '{task_name}' created successfully!")

    def assign_task(self, task_index, assignee):
        task_index = int(task_index) - 1
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["assignee"] = assignee
            print(
                f"Chatbot: Task '{self.tasks[task_index]['name']}' assigned to {assignee} successfully!"
            )
        else:
            print(
                "Chatbot: Invalid task index. Please check the task index and try again."
            )

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["status"] = "Complete"
            print(
                f"Chatbot: Task '{self.tasks[task_index]['name']}' marked as complete."
            )
        else:
            print(
                "Chatbot: Invalid task index. Please check the task index and try again."
            )

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            print(f"Chatbot: Task '{deleted_task['name']}' deleted successfully.")
        else:
            print(
                "Chatbot: Invalid task index. Please check the task index and try again."
            )

    def show_tasks(self):
        if not self.tasks:
            print("Chatbot: No tasks available.")
        else:
            print("Chatbot: Current Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(
                    f" {i}. {task['name']} | Status: {task['status']} | Assignee: {task.get('assignee', 'Unassigned')}"
                )


if __name__ == "__main__":
    task_chatbot = TaskChatbot()
    task_chatbot.start_chat()
