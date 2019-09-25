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
        const DateForm = ({begin, end, disabled}) => (
            <form onSubmit={(e) => this.getStats(e)} className="mb-2">
                        <DateRangePicker
                            onChange={(v) => this.updateField(v, 'range')}
                            required={true}
                            defaultValue={{begin, end}}
                            disabled={disabled}
                        />
                        <button
                            type="submit"
                            className="btn btn-primary"
                        >Загрузить</button>
                    </form>
        );

        if (status === 'FAILED') {
            return (
                <div className="alert alert-danger" role="alert">
                    <h4 className="alert-heading">Ошибка</h4>
                    <p>Не удалось загрузить данные. Попробуйте обновить страницу.</p>
                </div>
            );
        } else if (status === 'LOADING') {
            const {begin, end} = this.state.range || this.props.data;

            return (
                <React.Fragment>
                    <DateForm begin={begin} end={end} disabled={true}/>
                    <Loader/>
                </React.Fragment>
            );
        } else {
            const {type, stats} = this.props.data;
            const {begin, end} = this.state.range || this.props.data;

            return (
                <React.Fragment>
                    <DateForm begin={begin} end={end}/>
                    {type === 'API' ?
                        <ApiStats stats={stats}/> :
                        <TgBotStats stats={stats}/>}
                </React.Fragment>
            );
        }
    }
}

export default connect(
    mapStateToProps,
    {getStats: getData}
)(Stats);
