from aiogram import F
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from src.telegram.output.output_mess import OutputMessage as om

router = Router()


@router.message(Command('start'))
async def start_handler(message: types.Message) -> None:
    """
    Обрабатывает start и выводит приветственное сообщение
    :param message: Принимает сообщение пользователя
    :return: None
    """
    await message.answer(om.opening_greeting)


@router.message(F.text.lower() == 'главное меню')
@router.message(Command('menu'))
async def main_menu_handler(message: types.Message, state: FSMContext) -> None:
    """
    Обрабатывает команду возврата в главное меню, сбрасывает все стейты
    :param message: Принимает сообщение пользователя
    :param state: Принимает состояние
    :return: None
    """
    await state.clear()
    await message.answer(om.return_to_main_menu)
