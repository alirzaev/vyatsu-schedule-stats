import React from 'react';
import ReactDOM from 'react-dom';
import {Provider} from 'react-redux';

import Stats from './Stats';
import store from './store';
import './index.css';

ReactDOM.render(
    <Provider store={store}>
        <Stats/>
    </Provider>,
    document.getElementById('root')
);
