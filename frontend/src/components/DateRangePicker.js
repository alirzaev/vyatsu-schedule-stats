import React from 'react';

export default class DateRangePicker extends React.Component {
    constructor(props) {
        super(props);

        const {begin, end} = this.props.defaultValue;
        this.state = {begin, end};
    }

    updateField(event, field) {
        const value = event.target.value;

        this.setState(() => {
            return {[field]: value};
        });

        const defaultValue = this.props.defaultValue;

        this.props.onChange({
            begin: this.state.begin || defaultValue.begin,
            end: this.state.end || defaultValue.end,
            [field]: value
        });
    }

    render() {
        return (
            <div className="d-block">
                <div className="form-group row">
                    <label
                        htmlFor="begin"
                        className="col-2 col-form-label"
                    >От: </label>
                    <input
                        id="begin"
                        name="begin"
                        type="date"
                        className="form-control col mr-3"
                        defaultValue={this.props.defaultValue.begin}
                        onChange={(e) => this.updateField(e, 'begin')}
                        required={this.props.required}
                    />
                </div>
                <div className="form-group row">
                    <label
                        htmlFor="end"
                        className="col-2 col-form-label"
                    >До: </label>
                    <input
                        id="end"
                        name="end"
                        type="date"
                        className="form-control col mr-3"
                        defaultValue={this.props.defaultValue.end}
                        onChange={(e) => this.updateField(e, 'end')}
                        required={this.props.required}
                    />
                </div>
            </div>
        );
    }
}