import json
from pathlib import Path
from tkinter import messagebox
from typing import Optional

import customtkinter as ctk

from models.task import Task


class BoardApp(ctk.CTk):
    STATUSES = [
        "Backlog",
        "To do",
        "In progress",
        "Testing",
        "Done",
    ]

    def __init__(self) -> None:
        super().__init__()

        self.title("Python Kanban Board")
        self.geometry("1250x700")
        self.minsize(950, 550)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.tasks: list[Task] = []

        self.column_frames: dict[str, ctk.CTkScrollableFrame] = {}
        self.column_containers: dict[str, ctk.CTkFrame] = {}

        self.dragged_task: Optional[Task] = None
        self.dragged_card: Optional[ctk.CTkFrame] = None
        self.drag_preview: Optional[ctk.CTkFrame] = None

        self.drag_offset_x = 0
        self.drag_offset_y = 0

        project_root = Path(__file__).resolve().parent.parent
        self.data_file = project_root / "data" / "tasks.json"

        self.create_header()
        self.create_board()

        self.load_tasks()
        self.refresh_board()

    def create_header(self) -> None:
        header_frame = ctk.CTkFrame(self)
        header_frame.pack(
            fill="x",
            padx=15,
            pady=15,
        )

        title_label = ctk.CTkLabel(
            header_frame,
            text="Python Kanban Board",
            font=ctk.CTkFont(
                size=24,
                weight="bold",
            ),
        )
        title_label.pack(
            side="left",
            padx=15,
            pady=15,
        )

        self.task_entry = ctk.CTkEntry(
            header_frame,
            placeholder_text="Enter task title...",
            width=350,
        )
        self.task_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=10,
            pady=15,
        )

        self.task_entry.bind(
            "<Return>",
            lambda event: self.add_task(),
        )

        add_button = ctk.CTkButton(
            header_frame,
            text="Add task",
            command=self.add_task,
        )
        add_button.pack(
            side="left",
            padx=15,
            pady=15,
        )

    def create_board(self) -> None:
        board_frame = ctk.CTkFrame(self)
        board_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(0, 15),
        )

        board_frame.grid_rowconfigure(0, weight=1)

        for index, status in enumerate(self.STATUSES):
            board_frame.grid_columnconfigure(
                index,
                weight=1,
                uniform="columns",
            )

            column_container = ctk.CTkFrame(
                board_frame,
                corner_radius=10,
            )
            column_container.grid(
                row=0,
                column=index,
                padx=6,
                pady=10,
                sticky="nsew",
            )

            self.column_containers[status] = column_container

            column_title = ctk.CTkLabel(
                column_container,
                text=status,
                font=ctk.CTkFont(
                    size=18,
                    weight="bold",
                ),
            )
            column_title.pack(pady=10)

            tasks_frame = ctk.CTkScrollableFrame(
                column_container,
                fg_color="transparent",
            )
            tasks_frame.pack(
                fill="both",
                expand=True,
                padx=8,
                pady=(0, 8),
            )

            self.column_frames[status] = tasks_frame

    def add_task(self) -> None:
        task_title = self.task_entry.get().strip()

        if not task_title:
            messagebox.showwarning(
                "Missing task title",
                "Enter a task title.",
            )
            return

        task = Task(
            title=task_title,
            status="Backlog",
        )

        self.tasks.append(task)
        self.task_entry.delete(0, "end")

        self.save_tasks()
        self.refresh_board()

    def refresh_board(self) -> None:
        for column_frame in self.column_frames.values():
            for widget in column_frame.winfo_children():
                widget.destroy()

        for task in self.tasks:
            self.create_task_card(task)

    def create_task_card(self, task: Task) -> None:
        column_frame = self.column_frames[task.status]

        card = ctk.CTkFrame(
            column_frame,
            corner_radius=10,
            border_width=1,
        )
        card.pack(
            fill="x",
            padx=5,
            pady=7,
        )

        drag_area = ctk.CTkFrame(
            card,
            fg_color="transparent",
            cursor="hand2",
        )
        drag_area.pack(
            fill="x",
            padx=8,
            pady=(8, 4),
        )

        drag_icon = ctk.CTkLabel(
            drag_area,
            text="⠿",
            width=25,
            cursor="hand2",
            font=ctk.CTkFont(size=18),
        )
        drag_icon.pack(
            side="left",
            padx=(0, 5),
        )

        task_label = ctk.CTkLabel(
            drag_area,
            text=task.title,
            wraplength=170,
            justify="left",
            anchor="w",
            cursor="hand2",
        )
        task_label.pack(
            side="left",
            fill="x",
            expand=True,
        )

        status_menu = ctk.CTkOptionMenu(
            card,
            values=self.STATUSES,
            command=lambda selected_status: self.change_task_status(
                task,
                selected_status,
            ),
        )
        status_menu.set(task.status)
        status_menu.pack(
            fill="x",
            padx=10,
            pady=5,
        )

        delete_button = ctk.CTkButton(
            card,
            text="Delete",
            height=28,
            command=lambda: self.delete_task(task),
            fg_color="darkred",
            hover_color="red",
        )
        delete_button.pack(
            fill="x",
            padx=10,
            pady=(5, 10),
        )

        draggable_widgets = [
            card,
            drag_area,
            drag_icon,
            task_label,
        ]

        for widget in draggable_widgets:
            widget.bind(
                "<ButtonPress-1>",
                lambda event,
                selected_task=task,
                selected_card=card:
                self.start_drag(
                    event,
                    selected_task,
                    selected_card,
                ),
            )

            widget.bind(
                "<B1-Motion>",
                self.drag_task,
            )

            widget.bind(
                "<ButtonRelease-1>",
                self.drop_task,
            )

    def change_task_status(
        self,
        task: Task,
        new_status: str,
    ) -> None:
        if new_status == task.status:
            return

        task.status = new_status
        self.save_tasks()
        self.refresh_board()

    def start_drag(
        self,
        event,
        task: Task,
        card: ctk.CTkFrame,
    ) -> None:
        self.dragged_task = task
        self.dragged_card = card

        card.update_idletasks()

        card_width = max(
            card.winfo_width(),
            180,
        )

        card_x_root = card.winfo_rootx()
        card_y_root = card.winfo_rooty()

        self.drag_offset_x = event.x_root - card_x_root
        self.drag_offset_y = event.y_root - card_y_root

        card.pack_forget()

        self.drag_preview = ctk.CTkFrame(
            self,
            width=card_width,
            height=72,
            corner_radius=10,
            border_width=2,
        )
        self.drag_preview.pack_propagate(False)

        preview_label = ctk.CTkLabel(
            self.drag_preview,
            text=f"⠿  {task.title}\nStatus: {task.status}",
            justify="left",
            anchor="w",
            wraplength=max(card_width - 24, 150),
            font=ctk.CTkFont(size=14),
        )
        preview_label.pack(
            fill="both",
            expand=True,
            padx=12,
            pady=10,
        )

        self.move_preview(
            event.x_root,
            event.y_root,
        )

        self.drag_preview.lift()

    def drag_task(self, event) -> None:
        if self.drag_preview is None:
            return

        self.move_preview(
            event.x_root,
            event.y_root,
        )

        self.highlight_target_column(
            event.x_root,
            event.y_root,
        )

    def move_preview(
        self,
        x_root: int,
        y_root: int,
    ) -> None:
        if self.drag_preview is None:
            return

        x = (
            x_root
            - self.winfo_rootx()
            - self.drag_offset_x
        )

        y = (
            y_root
            - self.winfo_rooty()
            - self.drag_offset_y
        )

        self.drag_preview.place_configure(
            x=x,
            y=y,
        )

        self.drag_preview.lift()

    def drop_task(self, event) -> None:
        if self.dragged_task is None:
            return

        target_status = self.get_status_under_cursor(
            event.x_root,
            event.y_root,
        )

        if target_status is not None:
            self.dragged_task.status = target_status
            self.save_tasks()

        self.clear_column_highlights()

        if self.drag_preview is not None:
            self.drag_preview.destroy()

        self.drag_preview = None
        self.dragged_task = None
        self.dragged_card = None

        self.refresh_board()

    def get_status_under_cursor(
        self,
        x_root: int,
        y_root: int,
    ) -> Optional[str]:
        for status, container in self.column_containers.items():
            container.update_idletasks()

            left = container.winfo_rootx()
            top = container.winfo_rooty()

            right = left + container.winfo_width()
            bottom = top + container.winfo_height()

            cursor_inside = (
                left <= x_root <= right
                and top <= y_root <= bottom
            )

            if cursor_inside:
                return status

        return None

    def highlight_target_column(
        self,
        x_root: int,
        y_root: int,
    ) -> None:
        target_status = self.get_status_under_cursor(
            x_root,
            y_root,
        )

        for status, container in self.column_containers.items():
            if status == target_status:
                container.configure(border_width=2)
            else:
                container.configure(border_width=0)

    def clear_column_highlights(self) -> None:
        for container in self.column_containers.values():
            container.configure(border_width=0)

    def delete_task(self, task: Task) -> None:
        should_delete = messagebox.askyesno(
            "Delete task",
            f"Do you want to delete task:\n\n{task.title}?",
        )

        if not should_delete:
            return

        self.tasks.remove(task)
        self.save_tasks()
        self.refresh_board()

    def load_tasks(self) -> None:
        self.data_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self.data_file.exists():
            self.data_file.write_text(
                "[]",
                encoding="utf-8",
            )
            return

        try:
            file_content = self.data_file.read_text(
                encoding="utf-8",
            )

            tasks_data = json.loads(file_content)

            self.tasks = [
                Task.from_dict(task_data)
                for task_data in tasks_data
            ]

        except (
            json.JSONDecodeError,
            KeyError,
            TypeError,
        ):
            messagebox.showerror(
                "Data error",
                "Could not load tasks.json. "
                "The file may be corrupted.",
            )

            self.tasks = []

    def save_tasks(self) -> None:
        self.data_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        tasks_data = [
            task.to_dict()
            for task in self.tasks
        ]

        self.data_file.write_text(
            json.dumps(
                tasks_data,
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )