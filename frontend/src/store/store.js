import {actionsReducer} from "./reducers";
import {applyMiddleware, createStore} from 'redux';
import thunk from "redux-thunk";


export const store = createStore(
    actionsReducer, applyMiddleware(thunk)
);