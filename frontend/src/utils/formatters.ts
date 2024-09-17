import dayjs from 'dayjs';

export function formatDate(dateString: string): string {
  return dayjs(dateString).format('MMMM D, YYYY');
}

export function formatCurrency(amount: number, currencyCode: string): string {
  const formatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: currencyCode,
  });
  return formatter.format(amount);
}