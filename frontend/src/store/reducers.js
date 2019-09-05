import {fromJS} from "immutable";
import {SET_DATA, SET_STATUS} from "./actions";


const initialState = fromJS({
    data: {},
    status: 'LOADING'
});

export function actionsReducer(state = initialState, action) {
    const {type, payload} = action;

    if (type === SET_DATA) {
        const {data} = payload;
        state = state.set('data', data);
    } else if (type === SET_STATUS) {
        const {status} = payload;
        state = state.set('status', status);
    }

    return state;
}
