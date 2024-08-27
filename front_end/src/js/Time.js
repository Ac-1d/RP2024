export function currentTime() {
  const datetime = new Date();
  return timestampToTime(datetime);
}
function timestampToTime(date) {
  var Y = date.getFullYear() + '-';
  var M = (date.getMonth()+1 < 10 ? '0'+(date.getMonth()+1):date.getMonth()+1) + '-';
  var D = (date.getDate()< 10 ? '0'+date.getDate():date.getDate())+ ' ';
  var h = (date.getHours() < 10 ? '0'+date.getHours():date.getHours())+ ':';
  var m = (date.getMinutes() < 10 ? '0'+date.getMinutes():date.getMinutes()) + ':';
  var s = date.getSeconds() < 10 ? '0'+date.getSeconds():date.getSeconds();
  return Y+M+D+h+m+s;
}
export function extractDateTime(isoString) {  
  // 创建Date对象  
  const date = new Date(isoString);  

  // 验证Date对象是否有效  
  if (isNaN(date.getTime())) {  
      // throw new Error('Invalid date string');  
      return;
  }  

  // 提取并格式化日期和时间  
  const year = String(date.getUTCFullYear()).padStart(4, '0');  
  const month = String(date.getUTCMonth() + 1).padStart(2, '0'); // 月份从0开始，所以需要+1  
  const day = String(date.getUTCDate()).padStart(2, '0');  
  const hours = String(date.getUTCHours()).padStart(2, '0');  
  const minutes = String(date.getUTCMinutes()).padStart(2, '0');  
  const seconds = String(date.getUTCSeconds()).padStart(2, '0');  

  // 组合日期和时间字符串  
  const dateTimeString = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;  

  return dateTimeString;  
}  