// // // let person = {
// // //     login: "sdhasf",
// // //     password: "sadfsd",

// // // };

// // // person.__proto__.color = "red";



// // addUser.prototype.getCalcAge = function(){
// //     return new Date().getFullYear = this.year;
// // }

// // let Alex = new addUser("Alex",1995);


// // console.log(Alex);
// // // personalbar.car = "gfvghg";

// // let person = {
// //     name:"tani",
// // };

// // console.log(person);

// // function addPerson(name, age) {
// //     return{
// //         name,
// //         age,
// //     }
// // }


// // addPerson.prototype.getCalcYear = function () {
// //     return 2000;
// // };

// // let albert = addPerson("albert", 21);


// // console.log(albert);
// // console.log(Alex.getCalcAge);

















// // function addUser(name, year = 1995) {
// //     this.name = name;
// //     this.year = year;
// // }


// // let obj = {};

// // obj.login = 123;


// // console.log(obj.login);

// // addUser.prototype.writeDelay = function () {
// //    setTimeout( () => {
// //     alert(this.year);
// //     console.log(this);
// //   }, 2000)
// // };






// // let person = new addUser("tima");



// // person.writeDelay();









// // class RootElement {
// //     constructor(tagname = "div"){
// //         this.$el = document.createElement(tagname);
// //     }

// //     hide () {
// //         this.$el.style.display = "none";
// //     }

// //     append(){
// //         document.querySelector("body").appendChild(this.$el);
// //     }

// //     changeBorder(){

// //     }
// // };




// // class Box extends RootElement{
// //     constructor(color, size = 150, tagname,){     // полеморфизм
// //         super(tagname);
// //         this.color = color;
// //         this.size = size;
// //     }


// //     create(){
       
// //         this.$el.style.background = this.color;
// //         this.$el.style.width = this.$el.style.height = this.size + "px";
// //         this.append();


// //     }


// //     changeBorder(border){
// //        this.$el.style.borderRadius = border + "px";

// //     }
// // }







// // let box = new Box ("red");


// // box.create();
// // box.changeBorder(20);
 





// // console.log(box);





// // const form = document.querySelector("form");

// // form.addEventListener("submit", (event) => {
// //     event.preventDefault();
    

// //     const title = form.title.value;
// //     const text = form.title.value;
// //     const description = form.title.value;


   
// //     SaveForm({ title, text, description });





// // });





// // function SaveForm(data) {
// //     const formData = {
// //         date: new Date().toLocaleTimeString(),
// //         ...data,
        
    
        
// //     };

// //     console.log(formData);
// // }

































































































// class Dropdown{
//     constructor(selector , options){
//         this.$el = document.querySelector(selector);
//         this.items = options.items;


//         this.$el.querySelector("dropdown__label").textContent = this.item[0].label;


//         this.$el.addEventListener("click", (event) => {
//             if(event.target.classList.contains("dropdown"));
//         })




      
//     }



//     open() {
//         this.$el.classList.add("open");
//     }

//     close(){
//         this.$el.classList.remove("open");
//     }
// }








// const dropdown = new Dropdown("#dropdown", {
//     items: [
//         {label: "Moscow", id: "msk" },
//         {label: " Sankt-Peterburg", id: "sqb"},
//     ],
// });






// // h/w
// let first = 0;
// let second = 0;
// let firstInt = setInterval(() => {
//     console.log(first++);
    
// }, 300);
// let secondInt = setInterval(() => {
//     console.log(second++);
    
// }, 500);

// end h/w














// 20november

// let prom = prompt("введите число");

// let body = document.querySelector("body");

// let pomise = new Promise(function (resolve, reject){
    
//     resolve();
// });

// pomise
//   .then(() => {
//     return new Promise((resolve, reject) => {
//         let first = first;

//         if(first <=0  ) {
            
//             reject(first);
//         } 
//     });
// }).then((value) =>  {
    
//     console.log(value);
// })
  
// .catch((error) => {                                 
//     return new Promise(( resolve, reject ) => {
        
//         resolve(error);

//     });

// })
// .finally(() => {
//     alert("программма выполнена");
// });

// end 20 november




document.querySelector("#load").addEventListener("click", load);
let input = document.querySelector("#val");


function load() {
    const url = "https://jsonplaceholder.typicode.com/users";

    fetch(url)
    .then(function (response) {
        console.log(response);
        return response.json();
    })
    .then((data) => {
      
        console.log(data);


        let $ul = document.querySelector("#list");

    
          let html = data.map((item ) => {
              if(item.id == input.value) {
                return `<li>${item.name}:<br>
                ${item.id};<br>
                ${item.phone};<br>
                ${item.email}.</li>`
              }
         
         
         
         });
         console.log(html.join(""));
         
         if(html.join(" ")) {
            $ul.innerHTML = html.join(" ");

         } else {
            $ul.innerText = "dont have user";


         }


    //    console.log(html.join(" "));
    //    $ul.innerHTML = html.join(" ");
    });
    
}


























// let promise = new Promise(function(resolve, reject) {
//     if(usepsho){
//         resolve(val)
//     } else {
//         reject(val);
//     }
// });







