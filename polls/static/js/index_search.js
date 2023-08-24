$(document).ready(function() {
       $.ajax({
        type: 'get',
        url: "index_search_list/",
        dataType: 'json',
        success: function(data) {
            let jrentList = data.jrent;
            let realList = data.real;
            let datalist = $('#map_search_list');

            $.each(jrentList, function(index, item) {
                const option = $('<option></option>');
                option.attr('value', item.bdnm + ' ' + item.gunm + ' ' + item.dongnm + ' ' + item.bn + '-' + item.sbn);
                datalist.append(option)
            });

            $.each(realList, function(index, item) {
                const option = $('<option></option>');
                option.attr('value', item.bdnm + ' ' + item.gunm + ' ' + item.dongnm + ' ' + item.bn + '-' + item.sbn);
                datalist.append(option)
            });
        },
        error: function() {
            console.log('에러')
        }
    });
});