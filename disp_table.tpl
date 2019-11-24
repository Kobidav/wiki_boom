
%# disp_table.tpl 
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css "integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
<h1 align="center" >{{name}}</h1>
<br>
 <br>
 <table align="center" border="1" cellpadding="3">
  <tr>
<th>ID</th>
<th>Page ID</th>
<th>0</th>
<th>Title</th>
   <th>Time</th>
 </tr>
%for r in rows:
 <tr>
 %for c in r:
    <td>{{c}}</td>
  %end
</tr>
%end
</table>

















