
let account_container = document.getElementById("account-container");
let ultimate_password = document.getElementById("confirmpass");
let universalpass = document.getElementById("universalpass");
let disclaimer = document.getElementById("password-instruction");
let encrypting_passowrd = false;
let site = document.getElementById("site");
let username = document.getElementById("username");
let password = document.getElementById("newpassword");
let generate = document.getElementById("generate");
let create_new_account = document.getElementById("sendnewaccount");

//Populate with accounts when the program is opened.
let ACCOUNTS;
get_accounts()
.then(r => {
	ACCOUNTS = r;
	populate(ACCOUNTS);
});




generate.addEventListener('click', function(){
	generate_random_password()
	.then(pass => {
		password.value = pass;
	});
})

create_new_account.addEventListener("click", function(){
	//If there are any empty inputs, dont do anything.
	if(password.value.length == 0 || username.value.length == 0 || site.value.lenth == 0){
		return 0;
	}
	disclaimer.innerText = "Confirm your password to add the new account.";
	encrypting_passowrd = true;
	ultimate_password.style.zIndex = 4;

});


function get_account_information(){
	ultimate_password.style.zIndex = 4;
	let hash = this.getElementsByClassName("infotag")[2].getAttribute("hashedpass")
	universalpass.setAttribute("hashedpass", hash);
	disclaimer.innerText = "Confirm your password to get this password copied to your clipboard.";
}




//Check if password is correct:
universalpass.addEventListener("input", function(){
	check_if_password_correct(this.value)
	.then( r => {
		if(r){

			if(encrypting_passowrd){
				encrypt_password(this.value, password.value)
				.then(encrypted_password => {
					eel.add_new_account(site.value, username.value, encrypted_password);
					encrypting_passowrd = false;
					disclaimer.innerText = '';
					let ACCOUNTS;
					ultimate_password.style.zIndex = 0;
					site.value = '';
					username.value = '';
					password.value = '';
					document.getElementById("navaccounts").style.zIndex = 2;
					location.reload();
				});
			}

			else{
				eel.decrypt(this.value, this.getAttribute("hashedpass"));
				eel.notify("Correct password");
				ultimate_password.style.zIndex = 0;
				
			}
			this.value = '';
			this.value = "";
			this.setAttribute("hashedpass", "");
			disclaimer.innerText = '';
		}
	});
});


async function generate_random_password(){
	let new_password = await eel.new_password()();
	return new_password;
}


async function check_if_password_correct(password){
	let correct = await eel.check_password(password)();
	return correct;
}

async function encrypt_password(key, password){
	let passw = await eel.encrypt(key, password)();
	return passw;
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