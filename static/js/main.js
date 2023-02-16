const quizData = [
    {
        question: "ich bin, du bist, er/sie/es ______",
        a: "sind",
        b: "ist",
        c: "bin",
        correct: "b",
    },
    {
        question: "was ____ du gesagt?",
        a: "sind",
        b: "bin",
        c: "hast",
        correct: "c",
    },
    {
        question: "ich mochte nicht!",
        a: "Я не сплю",
        b: "Мы знаем",
        c: "Я не хочу",
        correct: "c",
    },
    {
        question: "Niemand darf Saschas Fahrrad ______________.",
        a: "spielen",
        b: "fahren",
        c: "anfassen",
        correct: "b",
    },
    {
        question: "искать/найти",
        a: "gehen/fahren",
        b: "trinken/giessen",
        c: "suchen/finden",
        correct: "c",
    },
];

const quiz = document.getElementById('quiz');
const answerElements = document.querySelectorAll('.answer');
const questionElement = document.getElementById('question');
const a_text = document.getElementById('a_text');
const b_text = document.getElementById('b_text');
const c_text = document.getElementById('c_text');
const submit = document.getElementById('submit');

let currentQuiz = 0;
let score = 0;

loadQuiz();

function loadQuiz(){
    deselectAnswers();

    const currentQuizData = quizData[currentQuiz];

    questionElement.innerText = currentQuizData.question;
    a_text.innerText = currentQuizData.a;
    b_text.innerText = currentQuizData.b;
    c_text.innerText = currentQuizData.c;
}

function deselectAnswers(){
    answerElements.forEach(answerEl => answerEl.checked = false)
}

function getSelected(){
    let answer;

    answerElements.forEach(answerEl => {
        if(answerEl.checked){
            answer = answerEl.id;
        }
    });

    return answer;
}

submit.addEventListener('click', () => {
    const answer = getSelected();

    if(answer){
        if(answer === quizData[currentQuiz].correct){
            score++;
        }

        currentQuiz++;

        if(currentQuiz < quizData.length){
            loadQuiz();
        }
        else{
            quiz.innerHTML = `<h2>Ваш уровень составляеть ${score} из ${quizData.length} </h2>
            <button id="submit" onclick="location.reload()">Reload</button>
            `;
        }
    }
});
