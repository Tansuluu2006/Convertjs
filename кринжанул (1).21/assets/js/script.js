const $currencyEL_one = document.querySelector("#currency-one");
const $currencyEL_two = document.querySelector("#currency-two");
const $amountEL_one = document.querySelector("#amount-one");
const $amountEL_two = document.querySelector("#amount-two");


const $rateEL = document.querySelector("#rate");
const $swap = document.querySelector("#swap");


$currencyEL_one.addEventListener("change", calculate);
$currencyEL_two.addEventListener("change", calculate);
$amountEL_one.addEventListener("input", calculate);
$amountEL_two.addEventListener("input", calculate);



 async function calculate() {
    const currency_one = $currencyEL_one.value;
    const currency_two = $currencyEL_two.value;


//     fetch(`https://v6.exchangerate-api.com/v6/93535d7b245c553eab1e2218/latest/${currency_one}`)
//     .then((res) => {
//         return res.json();

//     })
//     .then((data) => {
//         console.log(data);
    //     const rate = data.conversion_rates[currency_two];



    //     $rateEL.innerText = `1 ${currency_one} = ${rate} ${currency_two}`;



    //     $amountEL_two.value = ($amountEL_one.value * rate).toFixed(2);
    // });
    
// }

let res = await fetch(`https://v6.exchangerate-api.com/v6/93535d7b245c553eab1e2218/latest/${currency_one}`);
let data = await res.json();

const rate = data.conversion_rates[currency_two];
console.log(data);
$rateEL.innerText = `1 ${currency_one} = ${rate} ${currency_two}`;
$amountEL_two.value = ($amountEL_one.value * rate).toFixed(2);
}

$swap.addEventListener("click" , () => {
    const temp = $currencyEL_one.value;


    $currencyEL_one.value = $currencyEL_two.value;
    $currencyEL_two.value = temp;

    calculate();
});


calculate();

