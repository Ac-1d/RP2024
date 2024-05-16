export function currentTime() {
  const datetime = new Date();
  return join([datetime.getMonth(), ' ', datetime.getDate(), ' ', datetime.getHours(),
    ' ', datetime.getMinutes(), ':', datetime.getSeconds(), ' ']);
}