$('#btn_submit').click(function(){
    SendData();
});


function SendData(){
    
    let pr_floor1 = $('#printer_floor1').prop('checked');
    let pr_floor2 = $('#printer_floor2').prop('checked');
    let pr_hr = $('#printer_hr').prop('checked');
    if(pr_floor1){
        let pr_name = $('#printer_floor1').val();
        let pg_number = $('#page_number').val();
        let result_data = {pg_number:pg_number, pr_name:pr_name};
        $.post('validate', result_data);
    }else if(pr_floor2){
        let pr_name = $('#printer_floor2').val();
        let pg_number = $('#page_number').val();
        let result_data = {pg_number:pg_number, pr_name:pr_name};
        $.post('validate', result_data);
    }else if (pr_hr) {
        let pr_name = $('#printer_hr').val();
        let pg_number = $('#page_number').val();
        let result_data = {pg_number:pg_number, pr_name:pr_name};
        $.post('validate', result_data);
    }   
}