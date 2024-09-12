**TOPIC : DJANGO SIGNALS**

Answer 1. Django signals, by default, run synchronously. This means the signal is triggered and processed within the same thread and request-response cycle as the action that initiated it. The signal handlers (receivers) are executed before the code that triggered the signal can proceed.
Code Snippet for this is avialable in SignalOne app models.py file.
Below is the screenshot of the code:-
![Screenshot (463)](https://github.com/user-attachments/assets/f07450c9-da28-44e0-b046-443b56768c30)



Answer 2. 
By default, Django signals execute in the same thread as the caller. This means that the signal handlers run within the same thread that initiated the signal, which can be verified by comparing the thread IDs of both the caller and the signal handler.
Code Snippet for this is avialable in SignalTwo app models.py file.
Below is the screenshot of the code:-
![Screenshot (464)](https://github.com/user-attachments/assets/12c00380-44be-4835-a431-10499f84d8b2)



Answer 3. By default, Django signals operate within the same database transaction as the caller. This means that any modifications made by the signal handler are included in the same transaction as the caller. If the transaction is rolled back, both the caller's changes and the signal handler's changes will be reverted.

This can be demonstrated by:
Using transaction.atomic() to create a transaction block.
Triggering a signal that makes changes to the database.
Forcing a rollback in the caller and verifying whether the signal handler's changes are also rolled back.
Code Snippet for this is avialable in SignalThree app models.py file.
Below is the screenshot of the code:-
![Screenshot (465)](https://github.com/user-attachments/assets/56f3d144-5c6c-4788-b633-8eb410d45a2c)


**TOPIC - CUSTOM CLASSES IN PYTHON**

Answer. The Rectangle class will still take length and width as initialization parameters.
Instead of using yield directly inside the __iter__ method, I'll introduce a separate internal list and iterate over that to return the values.
Code Snippet for this is avialable in Question2.py outside django app.
Below is the screenshot of the code:-
![Screenshot (466)](https://github.com/user-attachments/assets/4a949911-3764-404b-8914-bf3d42c40534)

