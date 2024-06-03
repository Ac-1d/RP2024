import axios from 'axios';  
// 跨域问题暂时通过代理解决了，但是部署之后还要用其他方法

// const replyLimitTime = 5000;// 5秒响应时间

// 查找全部小说类别
export async function category() {
  try {
    const category = await axios.get('/novels/category_all');
    return category.data;
  } catch (error) {
    console.error('Error fetching categories:', error); 
    return error.code;
  }
}

// 查找某一类的小说
export async function categoryNovels(category_id) {
  try {
    const categoryNovels = await axios.get(`/novels/category?id=${category_id}`);
    return categoryNovels.data;
  } catch (error) {
    console.error('Error fetching categorized novels:', error);  
    return error.code;
  }
}

// 按条件（作者名，id，小说名）
export async function novels(search) {
  try {
    const novel = await axios.get(`/novels/novel?search=${search}`);
    return novel.data;
  } catch (error) {
    console.error('Error fetching novel:', error);  
    return error.code;
  }
}

// 查找所有小说
export async function allNovels() {
  try {
    const novel = await axios.get(`/novels/novel`);
    return novel.data;
  } catch (error) {
    console.error('Error fetching novel:', error);  
    return error.code;
  }
}

// 查找小说详细信息
export async function novelDetail(novel_id) {
  try {
    return await axios.get(`/novels/detail?id=${novel_id}`).data;
  } catch (error) {
    console.error('Error fetching novel details:', error);  
    return error.code;
  }
}

// 查询全部章节
export async function novelChapter(novel_id) {
  try {
    return await axios.get(`/novels/chapter_list?id=${novel_id}`).data;
  } catch (error) {
    return error.code;
  }
}

// 查询某章某节内容
export async function novelContent(novel_id, chapter_id) {
  try {
    return await axios.get(`/novels/chapter?id=${novel_id}&chapter_id=${chapter_id}`);
  } catch (error) {
    return error.code;
  }
}

// 加入书架

// 上传评论

// 获取评论

// 提交、更新最近阅读

// 获取最新阅读

// 查询个人书架

// 注册
