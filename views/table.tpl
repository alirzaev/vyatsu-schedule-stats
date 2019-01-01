<table class="table table-sm table-bordered">
    <thead>
        <tr>
            % for item in data['head']:
            <th scope="col">{{item}}</th>
            % end
        </tr>
    </thead>
    <tbody>
        % for row in data['body']:
        <tr>
            % for col in row:
            <td>{{col}}</td>
            % end
        </tr>
        % end
    </tbody>
</table>