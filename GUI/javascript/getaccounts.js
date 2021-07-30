
let account_container = document.getElementById("account-container");
let ultimate_password = document.getElementById("confirmpass");
let universalpass = document.getElementById("universalpass");

function get_account_information(){
	ultimate_password.style.zIndex = 4;
	let hash = this.getElementsByClassName("infotag")[2].getAttribute("hashedpass")
	universalpass.setAttribute("hashedpass", hash);
}




//Check if password is correct:
universalpass.addEventListener("input", function(){
	check_if_password_correct(this.value)
	.then( r => {
		if(r){
			eel.decrypt(this.value, this.getAttribute("hashedpass"));
			eel.notify("Correct password");
			ultimate_password.style.zIndex = 0;
			this.value = "";
			this.setAttribute("hashedpass", "");
		}
	});
});


async function check_if_password_correct(password){
	let correct = await eel.check_password(password)();
	return correct;
}



//Populate feed with accounts.
function populate(account_list){
	account_container.innerHTML = '';
	for(account of account_list){
		//Create information container element 
		let account_info = document.createElement("div");
		account_info.classList.add("info-display");
		account_info.addEventListener("click", get_account_information);

		let site_tag = document.createElement("p");
		site_tag.classList.add("infotag");
		site_tag.innerText = 'Site: ' + account['site'];


		let name_tag = document.createElement("p");
		name_tag.classList.add("infotag");
		name_tag.innerText = 'User: ' + account['user'];


		let password_tag = document.createElement("p");
		password_tag.classList.add("infotag");
		password_tag.innerText = 'Password: *******';
		password_tag.setAttribute("hashedpass", account['hashed_password'])
		

		//Put elements together.
		account_info.appendChild(site_tag);
		account_info.appendChild(name_tag);
		account_info.appendChild(password_tag);


		//Add elements to the DOM.
		account_container.appendChild(account_info);
	}
}

	
async function get_accounts(){
	let accounts = await eel.get_accounts()();
	return accounts;
}

//Populate with accounts when the program is opened.
let ACCOUNTS;
get_accounts()
.then(r => {
	ACCOUNTS = r;
	populate(ACCOUNTS);
});



//Search accounts.
let search_bar = document.getElementById("searcbarinput");

//Change the feed everytime that the user types in the searchbar.
search_bar.addEventListener("input", function(){
	let current_input = search_bar.value;
	let search_options = [];
	for(account of ACCOUNTS){
		//Check if what the person is typing matches to the site or user.
		if(account['site'].indexOf(current_input) != -1 || account['user'].indexOf(current_input) != -1){
			search_options.push(account);
		}
	}

	//Populate the feed with all the matching options
	populate(search_options);
});