let tg = window.Telegram.WebApp;
tg.expand();
tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#2cab37";
let item = "";

let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");

btn1.addEventListener("click", function () {
    tg.MainButton.setText("Искать: Мат+Физика");
    item = "мат+физика";
    tg.MainButton.show();
});

btn2.addEventListener("click", function () {
    tg.MainButton.setText("Искать: Мат+Информ");
    item = "мат+информатика";
    tg.MainButton.show();
});

btn3.addEventListener("click", function () {
    tg.MainButton.setText("Искать: Химия+Биология");
    item = "химия+биология";
    tg.MainButton.show();
});

Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData(item);
});