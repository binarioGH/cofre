
let accountstab = document.getElementById("accounts-tab");
let settingstab = document.getElementById("settings-tab");
let last_password = document.getElementById("oldpassword");
let new_password = document.getElementById("setnewpassword");
let confirm_password = document.getElementById("confirmnewpass");
let error_message = document.getElementById("error-message-newpass");



async function check_password_is_set(){
	let password_is_set = await eel.is_checksum_empty()();
	if(!password_is_set){
		last_password.style.display = "none";
		error_message.innerText = "You haven't set a supreme password!"
		settingstab.click();
	}
}



check_password_is_set();