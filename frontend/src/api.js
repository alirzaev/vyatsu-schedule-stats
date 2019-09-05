import axios from 'axios';


export function get(id, begin, end) {
    return axios.get(`/api/stats/${id}`, {
        params: {begin, end}
    });
}