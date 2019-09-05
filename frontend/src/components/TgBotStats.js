import React from "react";

export default ({stats}) => {
    return (
        <React.Fragment>
            <h3>Статистика по пользователям:</h3>
            <p>Кол-во активных пользователей: {stats.users}</p>
            <h3>Статистика по командам:</h3>
            <table className="table table-sm table-bordered">
                <thead>
                <tr>
                    <th scope="col">Команда</th>
                    <th scope="col">Кол-во</th>
                </tr>
                </thead>
                <tbody>
                {stats.commands.map(({command, count}) => (
                    <tr>
                        <td>{command}</td>
                        <td>{count}</td>
                    </tr>
                ))}
                </tbody>
            </table>
        </React.Fragment>
    );
}
