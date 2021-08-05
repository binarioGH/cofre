
let accountstab = document.getElementById("accounts-tab");
let settingstab = document.getElementById("settings-tab");
let last_password = document.getElementById("oldpassword");
let new_password = document.getElementById("setnewpassword");
let new_random_passwords = document.getElementById("random-pass-new");
let change_master = document.getElementById("change-master-pass");
let confirm_password = document.getElementById("confirmnewpass");
let error_message = document.getElementById("error-message-newpass");
let password_is_set = true;


async function check_password_is_set(){
	password_is_set = await eel.is_checksum_empty()();
	if(!password_is_set){
		last_password.style.display = "none";
		error_message.innerText = "You haven't set a supreme password!"
		settingstab.click();
		eel.create_backup();

	}
}


check_password_is_set();


new_random_passwords.addEventListener("click", function(){
	generate_random_password()
	.then(password => {
		new_password.setAttribute('type', 'text');
		confirm_password.setAttribute('type', 'text');

		new_password.value = password;
		confirm_password.value = password;
	});
});


async function update_master_password(last_password, new_password){
	var r = await eel.change_master_password(last_password, new_password)();
	return r;
}

change_master.addEventListener("click", function(){
	let npassword1 = new_password.value;
	let npassword2 = confirm_password.value;
	if((npassword1.length < 25 || npassword2.length < 25)){
		error_message = "Your password has to be at least 25 characters long. Try with a phrase that you can remember.";
		new_password.style.color = 'red';
		confirm_password.style.color = 'red';
		return 0;
	}

	if(npassword1 != npassword2){
		error_message.innerText = "Passwords don't match.";
		new_password.style.color = 'red';
		confirm_password.style.color = 'red';
		return 0;
	}

	new_password.style.color = 'white';
	confirm_password.style.color = 'white';

	update_master_password(last_password.value, npassword1)
	.then(response => {
		if(response == 0){
			last_password.style.display = "inline-block";
			last_password.value = "";
			new_password.value = "";
			confirm_password.value = "";
			error_message.innerText = "";
			accountstab.click();
			location.reload();
			
		}
		else if(response == -1){
			error_message.innerText = "The passwords are the same.";
		}
		else if(response == -2){
			last_password.value = "";
			error_message.innerText = "Last password is incorrect.";
		}

	});

});