___________________________
####Участникам SQA-Days15!<br>
####Если вы слушатель мастер-класса ["Автоматизация для ленивых тестировщиков"](http://www.sqadays.com/talk.sdf/sqadays/sqa_days15/talks/16562) и хотите присоединиться к разработке и запуску тестов прямо в аудитории, то скачайте быстрый установщик окружения для Win7/8  [отсюда](https://drive.google.com/file/d/0B7OLmDFb2I-JU1M2NXBkVm9hUEU/edit?usp=sharing), а также поставьте [Firefox](https://download.mozilla.org/?product=firefox-stub&os=win&lang=ru) и [Notepad++](http://download.tuxfamily.org/notepadplus/6.5.5/npp.6.5.5.Installer.exe).
___________________________


<br>


####Инструкция по установке Python+Selenium+Behave для Win7/8 

####Установка Python3.4

* **Cкачайте Python 3.4.0:**
    * [Windows x86 MSI Installer](https://www.python.org/ftp/python/3.4.0/python-3.4.0.msi) для Windows х32; 
    * [Windows x86-64 MSI Installer](https://www.python.org/ftp/python/3.4.0/python-3.4.0.amd64.msi) для Windows х64;

* **Запустите установку Python 3.4.0**

    <i>По умолчанию путь для установки C:\Python34\, инструкция основана на предположении, что туда вы его и поставите)</i>;
* **Укажите путь до python в системную переменную PATH:**
    * Откройте командную строку (WIN+R cmd);
    * Введите команду: `setx PATH "%PATH%;C:\Python34;C:\Python34\Lib\;C:\Python34\Scripts\;"`;
    * Нажмите Enter;

         Должна появиться надпись "УСПЕХ", либо "SUCCESS":
         ![Консоль]( "Консоль")

         Если у вас возникла ошибка переполнения переменной (более 1024 знаков):
         ![Консоль]("Консоль")
    
         То вы можете: <br>
               -либо почистить PATH (только со знаем дела, не удалите лишнего) и вписать туда пути для python; <br>
               -либо полностью прописывать пути испольняемых файлов при их запуске через командную строку;

* **Убедитесь, что python работает**
   * Перезапустите командную строку;
   * Введите команду `python` <br>
   <i>(если не прописан PATH, то пишем полный путь: C:\Python34\python.exe).</i><br>
      Если все ОК, то вы увидите следующее:
![Консоль]( "Консоль")


####Установка Selenium + Behave

* Установите Selenium и Behave. Для этого поочередно выполните команды `pip install selenium` и `pip install behave`;

    
####Полезные ссылки (на английском!)
1. [Behave 1.2.3 documentation](http://pythonhosted.org/behave/) Все, что вам требуется знать о Behave.
2. [Selenium with Python](http://selenium-python.readthedocs.org/) Здесь можно подсмотреть методы WebDriver. Как перейти по ссылке, найти элемент на странице, заполнить поле и многое другое.

####Контакты
Оксана
oksana.h@ati.su, Skype: jarovnya

Катерина 
katerina@ati.su, Skype: ekaterinajj
