var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey)
var elements = stripe.elements();

var style = {
    base: {
        color: '#000',
        fontFamily: 'Work Sans,sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '20px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {
    style: style
});


card.mount('#card-element');


// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
        <span class="icon" role="alert">
        <i class="fas fa-times"></i>
        </span>
        <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
        }
});

var loading = function(isLoading) {
    if (isLoading) {
      // Disable the button and show a spinner
      document.querySelector("submit-button").disabled = true;
      document.querySelector("#spinner").classList.remove("hidden");
      document.querySelector("#button-text").classList.add("hidden");
    } else {
      document.querySelector("submit-button").disabled = false;
      document.querySelector("#spinner").classList.add("hidden");
      document.querySelector("#button-text").classList.remove("hidden");
    }
  };

// Shows a success message when the payment is complete
var orderComplete = function(paymentIntentId) {
    loading(false);
    document
      .querySelector(".result-message a")
      .setAttribute(
        "href",
        "https://dashboard.stripe.com/test/payments/" + paymentIntentId
      );
    document.querySelector(".result-message").classList.remove("hidden");
    document.querySelector("button").disabled = true;
  };

var form = document.getElementById("payment-form");
form.addEventListener("submit", function (event) {
    event.preventDefault();
    card.update({'disabled': true})
    // Complete payment when the submit button is clicked
    payWithCard(stripe, card, clientSecret);
    });
    // Calls stripe.confirmCardPayment
    // If the card requires authentication Stripe shows a pop-up modal to
    // prompt the user to enter authentication details without leaving your page.
    var payWithCard = function (stripe, card, clientSecret) {
        loading(true);
        stripe.confirmCardPayment(clientSecret, {
        payment_method: {
        card: card
        }
    })
    .then(function (result) {
    if (result.error) {
        // Show error to your customer
        var errorDiv = document.getElementById('card-errors');
        var html = `
            <span class="icon" role="alert">
            <i class="fas fa-times"></i>
            </span>
            <span>${result.error.message}</span>
            `;
        $(errorDiv).html(html);
        card.update({'disabled': false})
        $('#submit-button').attr('disabled', false)
    } else {
    // The payment succeeded!
        if (result.paymentIntent.id === 'succeeded'); {
          form.submit();
            }
        }
    });
}