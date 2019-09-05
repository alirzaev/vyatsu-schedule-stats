import React from 'react';
import Loader from './components/Loader';
import {connect} from 'react-redux';
import {getData} from "./store/actions";
import TgBotStats from "./components/TgBotStats";
import ApiStats from "./components/ApiStats";
import DateRangePicker from "./components/DateRangePicker";

const mapStateToProps = (state) => {
    return {
        status: state.get('status'),
        data: state.get('data')
    };
};

class Stats extends React.Component {
    constructor(props) {
        super(props);

        this.state = {};
    }

    componentDidMount() {
        const id = location.pathname.split('/').pop();

        this.props.getStats(id);
    }

    updateField(value, field) {
        this.setState(() => {
            return {[field]: value};
        });
    }

    getStats(event) {
        event.preventDefault();

        const id = location.pathname.split('/').pop();
        const {begin, end} = this.state.range || this.props.data;
        this.props.getStats(id, begin, end);
    }

    render() {
        const status = this.props.status;
        if (this.props.status === 'FAILED') {
            return <span>Ошибка</span>;
        } else {
            const {type, stats, begin, end} = this.props.data;

            return (
                <React.Fragment>
                    <form onSubmit={(e) => this.getStats(e)} className="mb-2">
                        <DateRangePicker
                            onChange={(v) => this.updateField(v, 'range')}
                            required={true}
                            defaultValue={{begin, end}}
                        />
                        <button
                            type="submit"
                            className="btn btn-primary"
                        >Загрузить</button>
                    </form>
                    {status === 'LOADING' ?
                        <Loader/> :
                        (type === 'API' ?
                                <ApiStats stats={stats}/> :
                                <TgBotStats stats={stats}/>
                        )
                    }
                </React.Fragment>
            );
        }
    }
}

export default connect(
    mapStateToProps,
    {getStats: getData}
)(Stats);
