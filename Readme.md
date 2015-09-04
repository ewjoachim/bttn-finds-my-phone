# Find my phone when I press the Bt.tn !

So on the one side, I've got a [Bt.tn](http://bt.tn), a device that is a Wi-Fi connected Button I can press.

On the other side, I've got an [iPhone](http://www.apple.com/fr/iphone/), which is nothing more than a sightly more complex button, and I keep wondering where it is in my appartment.

So the logical answer is "make a press on the bt.tn [play a sound](http://www.apple.com/fr/icloud/find-my-iphone.html) on the iPhone.". So that's what this software does.

## How ?

First, the [pyicloud](https://github.com/picklepete/pyicloud) package allows me to programmatically use icloud to make my phone ring even if it's in silence mode.

Then, a small [Django](https://www.djangoproject.com/) app will use this module upon reception of a POST request. The app is hosted on [Heroku](https://www.heroku.com/)

Finally, my Bt.tn is configured to call this POST url upon press.

And that's all.

## I want it too !

Steps are :

 1. Clone the repo. At this point, you can already run a local server to try out the app with an HTTP client
 2. Create a Heroku free account
 3. Follow the basic [Heroku tutorial](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
 4. Put the app on heroku, you should then have an url for your app. At this point, you can test it with an HTTP client (like [curl](http://curl.haxx.se/) or the [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop) chrome extension)
 5. Configure the button with the url ``https://your-server/find_my_phone/`` and the POST parameters
 6. Press the button

## You said parameters ?

Yes, on the HTTP POST, you're expected to include 3 parameters :

| Key        |                 Value                 |
|------------|:-------------------------------------:|
| email      |          iCloud login email           |
| password   |         iCloud login password         |
| phone_name | The exact name you gave to your phone |

So you'll use these parameters for both testing and in the bt.tn interface.

## And that's all ?

No, once you've done that, [drop me a line](https://twitter.com/Ewjoachim) and then we'll both be very happy.
