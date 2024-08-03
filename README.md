Информационная система учета поступления сырья, выпуска готовой продукции и продажи готовой продукции для предприятия по производству кондитерских изделий.
Для создания информационной системы был использован фреймворк Django. База данных написана с помощью инструмента Django ORM, который позволяет взаимодействовать с базой данных через объектно-ориентированный подход. Шаблоны страниц написаны на HTML.

Диаграмма вариантов использования:
![image](https://github.com/user-attachments/assets/82ed75ee-1533-4790-872f-d564d68e9dec)


Архитектура:


![image](https://github.com/user-attachments/assets/6ddb6bf1-ff13-46d1-a579-21a130e76c3b)


Модель данных:
![image](https://github.com/user-attachments/assets/fe660310-b41d-46d4-9d57-1c73354c9931)



Схема добавления нового документа о поступлении сырья:


![image](https://github.com/user-attachments/assets/cbad271f-f4a3-42b7-8e46-a5761a9d332a)



Схема добавления нового документа о выпуске готовой продукции:


![image](https://github.com/user-attachments/assets/95053cf0-1cbd-4b34-bda9-bddb032aac8e)


Схема добавления нового документа о продаже готовой продукции:


![image](https://github.com/user-attachments/assets/872ab393-6f1f-42b1-843a-cc56a10ba4f2)



Главная страница веб-приложения:

![image](https://github.com/user-attachments/assets/2dc1a78f-22ef-43b6-ad6d-911bbf24b3d6)



Страница просмотра данных из таблицы сырья:

![image](https://github.com/user-attachments/assets/b3650b0d-6496-4b03-8cbb-6436f657f32e)



Страница добавления данных в таблицу сырья:

![image](https://github.com/user-attachments/assets/23a425e3-90d5-473e-b35e-4685765ff39a)



Страница со списком документов:

![image](https://github.com/user-attachments/assets/e27442dd-943f-4a8a-93f5-a6d84de07de2)



Страница с полной информацией документа о выпуске готовой продукции:

![image](https://github.com/user-attachments/assets/0fed31c5-f840-4759-9867-e3725c06a4e4)
![image](https://github.com/user-attachments/assets/4b1d66ce-db58-44c7-9d54-17b879e10211)


Страница заполнения табличной части документа:

![image](https://github.com/user-attachments/assets/342908d5-e453-474a-b4cd-5f9ea09691b1)



Возможности изменения или удаления данных в базе данных доступны администратору информационной системы. Фреймворк Django имеет административную панель, которая предоставляет администратору удобный интерфейс, позволяя просматривать, добавлять, редактировать и удалять данные из базы данных, не затрагивая написанный код.


Страница администрирования Django:

![image](https://github.com/user-attachments/assets/c5f27137-cc39-4926-95cd-d7f7033495c2)
