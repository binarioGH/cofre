
let account_container = document.getElementById("account-container");


function get_account_information(){
	console.log("here");
	console.log(this.getElementsByClassName("infotag")[2].getAttribute('hashedpass'));
}


async function get_accounts(){
	let accounts = await eel.get_accounts()();
	for(account of accounts){
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


get_accounts();