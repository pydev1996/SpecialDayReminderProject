importScripts('https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js');

var firebaseConfig = {
  apiKey: "AIzaSyB5T5QLJrvz9pbNcT1PMWSjT5Svyp2c-I4",
  authDomain: "specialday-44fe2.firebaseapp.com",
  projectId: "specialday-44fe2",
  storageBucket: "specialday-44fe2.appspot.com",
  messagingSenderId: "930052022962",
  appId: "1:930052022962:web:a622346d4f2e82fb179fab",
  measurementId: "G-Q9XK52R69S"
  };

firebase.initializeApp(firebaseConfig);
const messaging=firebase.messaging();

messaging.setBackgroundMessageHandler(function (payload) {
    console.log(payload);
    const notification=JSON.parse(payload);
    const notificationOption={
        body:notification.body,
        icon:notification.icon
    };
    return self.registration.showNotification(payload.notification.title,notificationOption);
});