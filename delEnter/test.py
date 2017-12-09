import re
str = """

<tr>
			<td style="text-align: center;vertical-align: middle;" width="10%">1</td>
			<td style="text-align: center;vertical-align: middle;" width="50%"><img src="http://localhost:8000/static/dist/img/photo3.jpg" /></td>
			<td style="text-align: center;vertical-align: middle;" width="20%">1</td>
			<td style="text-align: center;vertical-align: middle;" width="20%">
				<span class="glyphicon glyphicon-pencil"></span>
				<span class="glyphicon glyphicon-trash" style="margin-left: 10px;"></span>
			</td>
		</tr>
"""

str = re.sub(r'\s+','',str)
print(str)

