async function record_form() {
    event.preventDefault();

    let w = document.forms["contact_form"]["fname"].value;
    let x = document.forms["contact_form"]["lname"].value;
    let y = document.forms["contact_form"]["email"].value;
    let z = document.forms["contact_form"]["message"].value;
    if (w == "" || x == "" || y == "" || z == "") {
        window.location.href = '/error'
        return false;
    }

    const sub = new FormData(contact_form);

    try {
        const response = await fetch("https://api.web3forms.com/submit", {
        method: "POST",
        // Set the FormData instance as the request body
        body: sub,
        });
        console.log(await response.json());
    } catch (e) {
        console.error(e);
    }

    window.location.href = '/'
}

  /* const form = document.querySelector('#form');
  form.addEventListener('submit', function() {
      event.preventDefault();
      const sub = new FormData(form);
      console.log(sub);
  }) */


