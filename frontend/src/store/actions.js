import {get} from "../api";


export const SET_DATA = 'SET_DATA';

export const SET_STATUS = 'SET_STATUS';

export function setStatus(status) {
    return {
        type: SET_STATUS,
        payload: {status}
    };
}

export function setData(data) {
    return {
        type: SET_DATA,
        payload: {data}
    };
}

export function getData(id, begin, end) {
    return (dispatch) => {
        dispatch(setStatus('LOADING'));

        return get(id, begin, end)
            .then(response => {
                dispatch(setData(response.data));
                dispatch(setStatus('SUCCEED'));
            })
            .catch(error => {
                console.log(error.response.statusText);
                dispatch(setData({}));
                dispatch(setStatus('FAILED'));
            });
    }
}
