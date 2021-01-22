import axios from 'axios'; // 액시오스

export default function customAxios(url, callback) {
    axios(
        {
            url: '/api' + url,
            method: 'post',
            baseURL: 'http://localhost:8080',
            withCredentials: true,
        }
    ).then(function (response) {
        callback(response.data);
    });
}