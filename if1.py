"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    try:
        age = int(input("Сколько Вам лет?: "))
    except(ValueError):
        print('Укажите возраст цифрами')
    
    text =''
    def why_are_you(age):
        if 0 <= age < 6:
            text = "Вы должны учиться в детском саду!"
        elif 6 <= age < 17:
            text = "Вы должны учиться в школе!"
        elif 17 <= age < 22:
            text = "Вы должны учиться в ВУЗе!"
        elif age >= 22:
            text = "Вам пора работать!"
        else:
            text = "Возраст принимается от 0 и до ~"
        return text
    answer = why_are_you(age)
    print(answer)



if __name__ == "__main__":
    main()
