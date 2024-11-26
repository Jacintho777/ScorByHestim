import flet as ft
from quiz_questions import Questions
import random

class QuizApp:
    def __init__(self):
        self.current_round = 0
        self.score = 0
        self.questions = Questions
        self.random_questions = random.choices(population=list(range(0,50)),k=5)
        self.current_question = self.random_questions[self.current_round]

    def quit_quizz(self,e):
        self.page.views.pop()
        self.page.update()

    def build_ui(self, page: ft.Page):
        """
        Builds the user interface for the quiz application.

        Args:
            page (ft.Page): The page object where the UI components will be added.
        """
        self.page  = page

        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.question_text = ft.Text(value=f"Question {self.current_round + 1}:{self.questions[self.current_question].text}" ,size=20, text_align=ft.TextAlign.CENTER)
        self.choice_buttons = []
        self.result_text = ft.Text(size=24, color=ft.colors.GREEN, text_align=ft.TextAlign.CENTER)

        for i in range(4):
            btn = ft.ElevatedButton(
                text = self.questions[self.current_question].choices[i],
                on_click=lambda e, idx=i: self.check_answer(idx),
                width=400
            )
            self.choice_buttons.append(btn)

        self.next_button = ft.ElevatedButton(
            "Question suivante",
            on_click=self.next_question,
            visible=False
        )

        self.restart_button = ft.ElevatedButton(
            "Recommencer",
            on_click=self.restart_quiz,
            visible=False
        )

        page.views.append(
            ft.View(
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                floating_action_button = ft.FloatingActionButton(
                        icon=ft.icons.ARROW_BACK,
                        on_click=self.quit_quizz,
                    ),
                route='/quizz_page',
                controls=[
                    ft.Column(
                        [
                            self.question_text,
                            *self.choice_buttons,
                            self.result_text,
                            self.next_button,
                            self.restart_button,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ]
            )
        )
    def display_question(self):
        if self.current_round < len(self.random_questions):
            self.show_question()
        else:
            self.show_final_results()
        self.update_ui()

    def show_question(self):
        question = self.questions[self.current_question]
        self.question_text.value = f"Question {self.current_round + 1}: {question.text}"
        for i, choice in enumerate(question.choices):
            self.choice_buttons[i].text = choice
            self.choice_buttons[i].disabled = False
        self.result_text.value = ""
        self.next_button.visible = False

    def update_ui(self):
        self.question_text.update()
        for btn in self.choice_buttons:
            btn.update()
        self.result_text.update()
        self.next_button.update()

    def check_answer(self, choice_index: int):
        self.update_score_and_result(choice_index)
        self.disable_choice_buttons()
        self.show_next_button()

    def update_score_and_result(self, choice_index: int):
        question = self.questions[self.current_question]
        if choice_index == question.correct_answer:
            self.score += 1
            self.result_text.value = "Correct! ✅"
            self.result_text.color = ft.colors.GREEN
        else:
            self.result_text.value = f"Incorrect! La bonne réponse était: {question.choices[question.correct_answer]} ❌"
            self.result_text.color = ft.colors.RED
        self.result_text.update()

    def disable_choice_buttons(self):
        for btn in self.choice_buttons:
            btn.disabled = True
            btn.update()

    def show_next_button(self):
        self.next_button.visible = True
        self.next_button.update()

    def next_question(self, e):
        self.current_round += 1
        if self.current_round < len(self.random_questions):
            self.current_question= self.random_questions[self.current_round]
        self.display_question()

    def show_final_results(self):
        percentage = (self.score / len(self.random_questions)) * 100
        self.question_text.value = "Quiz terminé!"
        for btn in self.choice_buttons:
            btn.visible = False
        self.result_text.value = f"Score final: {self.score}/{len(self.random_questions)} ({percentage:.1f}%)"
        if percentage<=50:
            self.result_text.color = ft.colors.RED
        else:
            self.result_text.color = ft.colors.GREEN
        self.next_button.visible = False
        self.restart_button.visible = True
        self.restart_button.update()

    def restart_quiz(self, e):
        """
        Restarts the quiz by resetting the current question and score, and making the choice buttons visible again.

        Args:
            e: The event object (not used in this method).
        """
        self.current_round = 0
        self.random_questions = random.choices(population=list(range(0,50)),k=5)
        self.current_question = self.random_questions[self.current_round]
        self.score = 0
        for btn in self.choice_buttons:
            btn.visible = True
        self.restart_button.visible = False
        self.restart_button.update()
        self.display_question()

# def main(page: ft.Page):
#     quiz = QuizApp()
#     quiz.build_ui(page)

# if __name__ == "__main__":
#     ft.app(target=main)