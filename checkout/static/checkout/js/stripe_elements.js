/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/js

    CSS from here:
    https://stripe.com/docs/stripe-js
*/

/* we are slicing the first and last characters to remove the " " around the key */
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconcolor: '#dc3545'
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');
