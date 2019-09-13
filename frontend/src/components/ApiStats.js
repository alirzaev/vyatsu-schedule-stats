import React from "react";

export default ({stats}) => {
    return (
        <React.Fragment>
            <details>
                <summary>
                    <h3 className="d-inline-block">Вызовы API</h3>
                </summary>
                <table className="table table-sm table-bordered">
                    <thead>
                    <tr>
                        <th scope="col">API endpoint</th>
                        <th scope="col">Кол-во</th>
                    </tr>
                    </thead>
                    <tbody>
                    {stats.endpoints.map(({endpoint, count}) => (
                        <tr>
                            <td>{endpoint}</td>
                            <td>{count}</td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </details>

            <details>
                <summary>
                    <h3 className="pt-1 d-inline-block">Часто загружаемые расписания</h3>
                </summary>
                <table className="table table-sm table-bordered">
                    <thead>
                    <tr>
                        <th scope="col">Расписание</th>
                        <th scope="col">Кол-во</th>
                    </tr>
                    </thead>
                    <tbody>
                    {stats.schedules.top.map(({schedule, count}) => (
                        <tr>
                            <td>{schedule}</td>
                            <td>{count}</td>
                        </tr>
                    ))}
                    <tr>
                        <td className="font-weight-bold">Всего:</td>
                        <td>{stats.schedules.total}</td>
                    </tr>
                    </tbody>
                </table>
            </details>


            <details>
                <summary>
                    <h3 className="pt-1 d-inline-block">Часто загружаемые кафедры</h3>
                </summary>
                <table className="table table-sm table-bordered">
                    <thead>
                    <tr>
                        <th scope="col">Кафедры</th>
                        <th scope="col">Кол-во</th>
                    </tr>
                    </thead>
                    <tbody>
                    {stats.departments.top.map(({department, count}) => (
                        <tr>
                            <td>{department}</td>
                            <td>{count}</td>
                        </tr>
                    ))}
                    <tr>
                        <td className="font-weight-bold">Всего:</td>
                        <td>{stats.departments.total}</td>
                    </tr>
                    </tbody>
                </table>
            </details>
        </React.Fragment>
    );
}