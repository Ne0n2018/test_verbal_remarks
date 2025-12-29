@echo off
echo ========================================
echo Запуск автотестов API + Allure отчёт
echo ========================================

:: Активируем виртуальное окружение (если используешь .venv)
call .venv\Scripts\activate

:: Очищаем старые результаты Allure
rmdir /s /q allure-results 2>nul
rmdir /s /q allure-report 2>nul

:: Запускаем тесты с генерацией результатов Allure
pytest -s -v --alluredir=allure-results --clean-alluredir

:: Проверяем, успешно ли прошли тесты
if %errorlevel% neq 0 (
    echo.
    echo ТЕСТЫ УПАЛИ! Отчёт всё равно открываем...
    echo.
)

:: Запускаем Allure отчёт (serve — самый удобный режим)
echo.
echo Открываем Allure отчёт в браузере...
allure serve allure-results

pause