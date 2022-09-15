import path from 'path'
// const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
const MONTHS = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二']


export const toTitleCase = (str: string) => str.replace(
      /\w\S*/g,
      function(txt) {
        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
      }
    )

export const getMonthName = (date: Date) => MONTHS[new Date(date).getMonth()]

export const getSlugFromPathname = (pathname: string) => path.basename(pathname, path.extname(pathname))
