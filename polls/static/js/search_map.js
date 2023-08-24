var htmlMarker1 = {
    content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(/static/images/map/cluster-marker-1.png);background-size:contain;"></div>',
    size: N.Size(40, 40),
    anchor: N.Point(20, 20)
},
    htmlMarker2 = {
    content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(/static/images/map/cluster-marker-2.png);background-size:contain;"></div>',
    size: N.Size(40, 40),
    anchor: N.Point(20, 20)
},
    htmlMarker3 = {
    content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(/static/images/map/cluster-marker-3.png);background-size:contain;"></div>',
    size: N.Size(40, 40),
    anchor: N.Point(20, 20)
},
    htmlMarker4 = {
    content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(/static/images/map/cluster-marker-4.png);background-size:contain;"></div>',
    size: N.Size(40, 40),
    anchor: N.Point(20, 20)
},
    htmlMarker5 = {
    content: '<div style="cursor:pointer;width:40px;height:40px;line-height:42px;font-size:10px;color:white;text-align:center;font-weight:bold;background:url(/static/images/map/cluster-marker-5.png);background-size:contain;"></div>',
    size: N.Size(40, 40),
    anchor: N.Point(20, 20)
};

// 마커 정보창
var infoWindow = new naver.maps.InfoWindow({});

// 마커 표시하고 숨기는 함수
function updateMarkers(map, markers) {

    var mapBounds = map.getBounds();
    var marker, position;

    for (var i = 0; i < markers.length; i++) {

        marker = markers[i]
        position = marker.getPosition();

        if (mapBounds.hasLatLng(position)) {
            showMarker(map, marker);
        } else {
            hideMarker(map, marker);
        }
    }
}

// 화면에서 보이는 영역 마커 표시 함수
function showMarker(map, marker) {
    if (marker.getMap()) return;
    marker.setMap(map);
}

// 화면에서 안보일 때 마커 숨기는 함수
function hideMarker(map, marker) {
    if (!marker.getMap()) return;
    marker.setMap(null);
}

// 주소로 지도 검색
function searchAddressToCoordinate(address, title) {
    naver.maps.Service.geocode({
        query: address
    }, function (status, response) {
        if (status === naver.maps.Service.Status.ERROR) {
            return alert('접속 실패!');
        }

        if (response.v2.meta.totalCount === 0) {
            return alert('찾지 못했습니다.');
        }

        var htmlAddresses = [],
            item = response.v2.addresses[0],
            point = new naver.maps.Point(item.x, item.y);

        map.setCenter(point);
        map.setZoom(14);
    });
}

// 지도의 현재 위치 찾는 코드
naver.maps.Event.once(map, 'init', function () {
    var customControl = new naver.maps.CustomControl(locationBtnHtml, {
        position: naver.maps.Position.RIGHT_CENTER
    });

    // 커서 스타일 설정
    customControl.getElement().style.cursor = 'pointer';

    customControl.setMap(map);

    naver.maps.Event.addDOMListener(customControl.getElement(), 'click', function () {

        function onSuccessGeolocation(position) {
            var location = new naver.maps.LatLng(position.coords.latitude,
                position.coords.longitude);

            map.setCenter(location); // 얻은 좌표를 지도의 중심으로 설정합니다.
            map.setZoom(14); // 지도의 줌 레벨을 변경합니다.

        }

        function onErrorGeolocation() {
            var center = map.getCenter();
        }

        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(onSuccessGeolocation, onErrorGeolocation);
        } else {
            var center = map.getCenter();
        }
    });
});

var all_markers = [],
    markerGroup1 = [],
    markerGroup2 = [],
    markerGroup3 = [],
    markerGroup4 = [];

// 마커 클러스터링 업데이트 함수
function updateMarkerClustering(markers) {

    // 새로운 MarkerClustering 인스턴스 생성
    markerClustering = new MarkerClustering({
    minClusterSize: 3,
    maxZoom: 17,
    map: map,
    markers: markers,
    disableClickZoom: true,
    gridSize: 150,
    icons: [htmlMarker1, htmlMarker2, htmlMarker3, htmlMarker4, htmlMarker5],
    indexGenerator: [10, 100, 200, 500, 1000],
    stylingFunction: function(clusterMarker, count) {
      $(clusterMarker.getElement()).find('div:first-child').text(count);
    },
    minClusterZIndex: 100,
    maxClusterZIndex: 200
    });
}

// 마커 및 마커 이벤트 생성 함수
function createMarker(lat, lng, iconUrl, text, text_list) {
    var marker = new naver.maps.Marker({
        position: new naver.maps.LatLng(lng, lat),
        map: map,
        icon: {
        url: iconUrl,
        size: new naver.maps.Size(50, 50),
        origin: new naver.maps.Point(0, 0),
        anchor: new naver.maps.Point(25, 50)
        }
    });

    naver.maps.Event.addListener(marker, 'click', function() {
        // 정보창 생성
        infoWindow.setContent('<div style="display: inline-block; width: 200px; height: 50px; background: #f2f2f2; border: 2px solid #ddd; border-radius: 10px; color: #333; font-weight: bold; box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2); text-align: center; vertical-align: middle; line-height: 50px;">' + text + '</div>') // 정보창에 표시할 내용
        infoWindow.setOptions({
            borderWidth: 0
        });

        // 마커에 정보창 표시
        infoWindow.open(map, marker);

        $('#map_search_print').empty();
        if(text_list.length > 0) {
            $('#map_search_print').append('<li>접수연도: ' + text_list[0] + '</li>');
            $('#map_search_print').append('<li>주소: ' + text_list[1] + '</li>');
            $('#map_search_print').append('<li>건물명: ' + text_list[2] + '</li>');

            var dateStr = text_list[3];
            var year = dateStr.slice(0, 4);
            var month = dateStr.slice(4, 6);
            var day = dateStr.slice(6, 8);
            var formattedDate = year + '-' + month + '-' + day;

            $('#map_search_print').append('<li>계약일: ' + formattedDate + '</li>');

            // 추가 동작 수행
            if (text_list[text_list.length - 1] === '2') {
                $('#map_search_print').append('<li>전월세구분: ' + text_list[4] + '</li>');
                var deposit = Number(text_list[5]).toLocaleString();
                $('#map_search_print').append('<li>보증금(만원): ' + deposit + '</li>');
                var rent = Number(text_list[6]).toLocaleString();
                $('#map_search_print').append('<li>임대료(만원): ' + rent + '</li>');
                $('#map_search_print').append('<li>임대면적: ' + text_list[7] + '㎡</li>');
                $('#map_search_print').append('<li>층: ' + text_list[8] + '</li>');
                $('#map_search_print').append('<li>건축년도: ' + text_list[9] + '</li>');
                $('#map_search_print').append('<li>건물용도: ' + text_list[10] + '</li>');
                $('#map_search_print').append('<li>신규갱신여부: ' + text_list[11] + '</li>');
                $('#map_search_print').append('<li>계약갱신권사용여부: ' + text_list[12] + '</li>');
                $('#map_search_print').append('<li>종전보증금: ' + text_list[13] + '</li>');
                $('#map_search_print').append('<li>종전임대료: ' + text_list[14] + '</li>');
            } else {
                $('#map_search_print').append('<li>권리구분: ' + text_list[4] + '</li>');
                var sale = Number(text_list[5]).toLocaleString();
                $('#map_search_print').append('<li>물건금액(만원): ' + sale + '</li>');
                $('#map_search_print').append('<li>건물면적: ' + text_list[6] + '㎡</li>');
                $('#map_search_print').append('<li>토지면적: ' + text_list[7] + '㎡</li>');
                $('#map_search_print').append('<li>층: ' + text_list[8] + '</li>');
                $('#map_search_print').append('<li>취소일: ' + text_list[9] + '</li>');
                $('#map_search_print').append('<li>건축년도: ' + text_list[10] + '</li>');
                $('#map_search_print').append('<li>건물용도: ' + text_list[11] + '</li>');
                $('#map_search_print').append('<li>신고구분: ' + text_list[12] + '</li>');
            }
        }
    });

    return marker;
};

// 메인 페이지 지도 검색
function searchAddress(queryValue) {
    $.ajax({
        type: "get",
        url: "map_search/",
        dataType: "json",
        data: { query: queryValue },
        success: function(data) {
            if (data.items.length > 0) {
                searchAddressToCoordinate(data.items[0].address, data.items[0].title);
            } else {
                searchAddressToCoordinate(query, query);
            }
        },
        error: function() {
            console.log('확인 불가');
        }
    });
}

$(document).ready(function() {
    // 현재 URL의 쿼리 문자열 가져오기
    var queryString = window.location.search;

    // URLSearchParams 객체 생성
    var params = new URLSearchParams(queryString);

    // 특정 매개변수의 값을 가져오기
    var queryValue = params.get('search_data');

    searchAddress(queryValue);
    searchAddressToCoordinate('서울 강남구 테헤란로5길 24 장연빌딩', '강남 그린컴퓨터아카데미');

    // 미리 만든 4개의 배열
    var markerGroups = {
        group1: markerGroup1,
        group2: markerGroup2,
        group3: markerGroup3,
        group4: markerGroup4
    };

    $('.map_grouping input[type="radio"]').click(function() {
        var selectedMarkerGroupId = this.value;

        // 선택된 마커 그룹 배열 가져오기
        var selectedMarkerGroup = markerGroups[selectedMarkerGroupId];

        // 현재 상태 확인
        var isMarkersVisible = selectedMarkerGroup.some(function(marker) {
            return marker.getVisible();
        });

        // 선택된 마커 그룹의 마커 보이기/숨기기 토글
        selectedMarkerGroup.forEach(function(marker) {
            marker.setVisible(!isMarkersVisible);
        });
    });
})

$.ajax({
    type: 'get',
    url: "map_convert/",
    dataType: 'json',
    success: function(data) {
        var count1 = 0;
        var count2 = 0;
        var lat;
        var lng;
        var text;
        var iconUrl;
        var marker;

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

        for (var i=0; i<data.real.length; i++) {

            var text_list = [];

            switch (data.real[i].bdusa) {
                case '연립다세대':
                    iconUrl = "/static/images/map/icon2.png";
                    lat = data.real[i].lat;
                    lng = data.real[i].lng;
                    text = data.real[i].bdnm;

                    text_list.push(data.real[i].year);
                    text_list.push(data.real[i].gunm + ' ' + data.real[i].dongnm + ' ' + data.real[i].bn + '-' + data.real[i].sbn);
                    text_list.push(data.real[i].bdnm);
                    text_list.push(data.real[i].cont);
                    text_list.push(data.real[i].authr);
                    text_list.push(data.real[i].depos);
                    text_list.push(data.real[i].spa);
                    text_list.push(data.real[i].spa2);
                    text_list.push(data.real[i].fl);
                    text_list.push(data.real[i].cancel);
                    text_list.push(data.real[i].bdcont);
                    text_list.push(data.real[i].bdusa);
                    text_list.push(data.real[i].noti);
                    text_list.push(data.real[i].distin);

                    marker = createMarker(lat, lng, iconUrl, text, text_list);

                    markerGroup1.push(marker);
                    all_markers.push(marker);
                    count1++;
                    break;
                case '아파트':
                    iconUrl = "/static/images/map/icon4.png";
                    lat = data.real[i].lat;
                    lng = data.real[i].lng;
                    text = data.real[i].bdnm;

                    text_list.push(data.real[i].year);
                    text_list.push(data.real[i].gunm + ' ' + data.real[i].dongnm + ' ' + data.real[i].bn + '-' + data.real[i].sbn);
                    text_list.push(data.real[i].bdnm);
                    text_list.push(data.real[i].cont);
                    text_list.push(data.real[i].authr);
                    text_list.push(data.real[i].depos);
                    text_list.push(data.real[i].spa);
                    text_list.push(data.real[i].spa2);
                    text_list.push(data.real[i].fl);
                    text_list.push(data.real[i].cancel);
                    text_list.push(data.real[i].bdcont);
                    text_list.push(data.real[i].bdusa);
                    text_list.push(data.real[i].noti);
                    text_list.push(data.real[i].distin);

                    marker = createMarker(lat, lng, iconUrl, text, text_list);

                    markerGroup2.push(marker);
                    all_markers.push(marker);
                    count1++;
                    break;
                case '오피스텔':
                    iconUrl = "/static/images/map/icon3.png";
                    lat = data.real[i].lat;
                    lng = data.real[i].lng;
                    text = data.real[i].bdnm;

                    text_list.push(data.real[i].year);
                    text_list.push(data.real[i].gunm + ' ' + data.real[i].dongnm + ' ' + data.real[i].bn + '-' + data.real[i].sbn);
                    text_list.push(data.real[i].bdnm);
                    text_list.push(data.real[i].cont);
                    text_list.push(data.real[i].authr);
                    text_list.push(data.real[i].depos);
                    text_list.push(data.real[i].spa);
                    text_list.push(data.real[i].spa2);
                    text_list.push(data.real[i].fl);
                    text_list.push(data.real[i].cancel);
                    text_list.push(data.real[i].bdcont);
                    text_list.push(data.real[i].bdusa);
                    text_list.push(data.real[i].noti);
                    text_list.push(data.real[i].distin);

                    marker = createMarker(lat, lng, iconUrl, text, text_list);

                    markerGroup3.push(marker);
                    all_markers.push(marker);
                    count1++;
                    break;
                default:
                    break;
            }

            if (count1 === 500) {
                break;
            }

        };

        for (var i=0; i<data.jrent.length; i++) {
            var text_list = [];

            switch (data.jrent[i].bdusa) {
                case '연립다세대':
                    iconUrl = "/static/images/map/icon2.png";
                    lat = data.jrent[i].lat;
                    lng = data.jrent[i].lng;
                    text = data.jrent[i].bdnm;

                    text_list.push(data.jrent[i].year);
                    text_list.push(data.jrent[i].gunm + ' ' + data.jrent[i].dongnm + ' ' + data.jrent[i].bn + '-' + data.jrent[i].sbn);
                    text_list.push(data.jrent[i].bdnm);
                    text_list.push(data.jrent[i].cont);
                    text_list.push(data.jrent[i].distin2);
                    text_list.push(data.jrent[i].depos);
                    text_list.push(data.jrent[i].depos2);
                    text_list.push(data.jrent[i].spa);
                    text_list.push(data.jrent[i].fl);
                    text_list.push(data.jrent[i].bdcont);
                    text_list.push(data.jrent[i].bdusa);
                    text_list.push(data.jrent[i].newcont);
                    text_list.push(data.jrent[i].newcont2);
                    text_list.push(data.jrent[i].olddepos);
                    text_list.push(data.jrent[i].olddepos2);
                    text_list.push(data.jrent[i].distin);

                    marker = createMarker(lat, lng, iconUrl, text, text_list);

                    markerGroup1.push(marker);
                    all_markers.push(marker);
                    count2++;
                    break;
                case '아파트':
                    iconUrl = "/static/images/map/icon4.png";
                    lat = data.jrent[i].lat;
                    lng = data.jrent[i].lng;
                    text = data.jrent[i].bdnm;

                    text_list.push(data.jrent[i].year);
                    text_list.push(data.jrent[i].gunm + ' ' + data.jrent[i].dongnm + ' ' + data.jrent[i].bn + '-' + data.jrent[i].sbn);
                    text_list.push(data.jrent[i].bdnm);
                    text_list.push(data.jrent[i].cont);
                    text_list.push(data.jrent[i].distin2);
                    text_list.push(data.jrent[i].depos);
                    text_list.push(data.jrent[i].depos2);
                    text_list.push(data.jrent[i].spa);
                    text_list.push(data.jrent[i].fl);
                    text_list.push(data.jrent[i].bdcont);
                    text_list.push(data.jrent[i].bdusa);
                    text_list.push(data.jrent[i].newcont);
                    text_list.push(data.jrent[i].newcont2);
                    text_list.push(data.jrent[i].olddepos);
                    text_list.push(data.jrent[i].olddepos2);
                    text_list.push(data.jrent[i].distin);

                    marker = createMarker(lat, lng, iconUrl, text, text_list);

                    markerGroup2.push(marker);
                    all_markers.push(marker);
                    count2++;
                    break;
                case '오피스텔':
                    iconUrl = "/static/images/map/icon3.png";
                    lat = data.jrent[i].lat;
                    lng = data.jrent[i].lng;
                    text = data.jrent[i].bdnm;

                    text_list.push(data.jrent[i].year);
                    text_list.push(data.jrent[i].gunm + ' ' + data.jrent[i].dongnm + ' ' + data.jrent[i].bn + '-' + data.jrent[i].sbn);
                    text_list.push(data.jrent[i].bdnm);
                    text_list.push(data.jrent[i].cont);
                    text_list.push(data.jrent[i].distin2);
                    text_list.push(data.jrent[i].depos);
                    text_list.push(data.jrent[i].depos2);
                    text_list.push(data.jrent[i].spa);
                    text_list.push(data.jrent[i].fl);
                    text_list.push(data.jrent[i].bdcont);
                    text_list.push(data.jrent[i].bdusa);
                    text_list.push(data.jrent[i].newcont);
                    text_list.push(data.jrent[i].newcont2);
                    text_list.push(data.jrent[i].olddepos);
                    text_list.push(data.jrent[i].olddepos2);
                    text_list.push(data.jrent[i].distin);

                    marker = createMarker(lat, lng, iconUrl, text, text_list);

                    markerGroup3.push(marker);
                    all_markers.push(marker);
                    count2++;
                    break;
                default:
                    break;
            }

            if (count2 === 1000) {
                break;
            }

        };

        // 마커 클러스터링 업데이트
        updateMarkerClustering(all_markers);

        // updateMarkers 스크롤 시 함수 실행
        naver.maps.Event.addListener(map, 'zoom_changed', function() {
            updateMarkers(map, all_markers);
            infoWindow.close();
        });

        naver.maps.Event.addListener(map, 'dragend', function() {
            updateMarkers(map, all_markers);
            infoWindow.close();
        });
    },
    error: function() {
        console.log('에러')
    }
});

$('form').on('submit', function(e) {
    e.preventDefault();
    var value = $('#map_address').val();

    $.ajax({
        type: "get",
        url: "map_search/",
        dataType: "json",
        data: {query:value},
        success: function(data) {
            if(data.items.length > 0) {
                searchAddressToCoordinate(data.items[0].address, data.items[0].title);
            }else {
                searchAddressToCoordinate(value, value);
            }
            $('#map_address').val('');
        },
        error: function() {
            console.log('확인 불가');
        }
    })
})
