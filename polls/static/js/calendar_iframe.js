$(document).ready(function() {
    function formatPhoneNumber(phoneNumber) {
        var cleaned = phoneNumber.replace(/\D/g, '');
        var formatPhNumber = '';

        if (phoneNumber.length > 10) {
            var formatPhNumber = cleaned.replace(/(\d{3})(\d{4})(\d{4})/, '$1-$2-$3');
        } else if (phoneNumber.length == 10) {
            var formatPhNumber = cleaned.replace(/(\d{3})(\d{3})(\d{4})/, '$1-$2-$3');
        } else if (phoneNumber.length == 9) {
            var formatPhNumber = cleaned.replace(/(\d{2})(\d{3})(\d{4})/, '$1-$2-$3');
        } else if (phoneNumber.length == 8) {
            var formatPhNumber = cleaned.replace(/(\d{4})(\d{4})/, '$1-$2');
        }
        return formatPhNumber;
    }
    var phoneNumElement = $('#ph_number');
    var phoneNumber = phoneNumElement.text();
    var formatPhNumber = formatPhoneNumber(phoneNumber);
    phoneNumElement.text(formatPhNumber);
    var phoneNum = $('#ph_num');
    var phone = phoneNum.text();
    var formatPh = formatPhoneNumber(phone);
    phoneNum.text(formatPh);

});