import axios from 'axios';

// 注册成为作者
export async function beAuthor(id) {
  try {
    // console.log({user_id: id});
    return await axios.post(`novels/author_register?user_id=${id}`);
  } catch(error) {
    // console.log(error);
    return error.code;
  }
}

// 获取作者信息
export async function authorInfo(user_id) {
  try {
    const authorinfo = await axios.get(`/novels/author_info?user_id=${user_id}`);
    return authorinfo.data;
  } catch (error) {
    console.error('Error getting authorInfo:', error); 
    return error.code;
  }
}

// 更新作者信息
export async function updateAuthorInfo(author_id, formData) {
  try {
    const reply = await axios.patch(`/novels/author_register?user_id=${author_id}`, formData);
    return reply.data.message;
  } catch(error) {
    return error.code;
  }
}

// 小说新建
export async function createNovel(formData) {
  try {
    const reply  = await axios.post(`/novels/create_novel?`, formData);
    return reply.data.message;
  } catch(error) {
    return error.code;
  }
} 

// 小说详情更新
export async function updateNovelInfo(novel_id, formData) {
  try {
    const reply = await axios.patch(`/novels/create_novel?novel_id=${novel_id}`, formData);
    return reply.data.message;
  } catch(error) {
    return error.code;
  }
} 

// 创建小说章节
export async function createChapter(formData) {
  try {
    const reply = await axios.post(`/novels/create_chapter`, formData);
    return reply.data.message;
  } catch(error) {
    return error.code;
  }
}

// 更新章节信息 /novels/create_chapter
export async function updateChapterInfo(novel_id, chapter_id, formData) {
  try {
    const reply = 
      await axios.patch(`/novels/create_chapter?novel_id=${novel_id}&chapter_id=${chapter_id}`, formData);
    return reply.data.message;
  } catch(error) {
    return error.code;
  }
}


// 查找全部小说类别
export async function category() {
  try {
    const response = await axios.get('/novels/category_all');
    return response.data;
  } catch (error) {
    console.error('Error fetching categories:', error);
    return error.code;
  }
}

// 查找某一类的小说
export async function categoryNovels(category_id) {
  try {
    const response = await axios.get(`/novels/category?id=${category_id}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching categorized novels:', error);
    return error.code;
  }
}

// 按条件（作者名，id，小说名）
export async function novels(search) {
  try {
    const response = await axios.get(`/novels/novel?search=${search}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching novel:', error);
    return error.code;
  }
}

// 查找所有小说
export async function allNovels() {
  try {
    const response = await axios.get(`/novels/novel`);
    return response.data;
  } catch (error) {
    console.error('Error fetching novel:', error);
    return error.code;
  }
}

// 查找小说详细信息
export async function novelDetail(novel_id) {
  try {
    const response = await axios.get(`/novels/detail?id=${novel_id}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching novel details:', error);
    return error.code;
  }
}

// 查询全部章节
export async function novelChapter(novel_id) {
  try {
    const response = await axios.get(`/novels/chapter_list?id=${novel_id}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching chapters:', error);
    return error.code;
  }
}

// 查询某章某节内容
export async function novelContent(novel_id, chapter_id) {
  try {
    const response = await axios.get(`/novels/chapter?id=${novel_id}&chapter_id=${chapter_id ? chapter_id : 1}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching chapter content:', error);
    return error.code;
  }
}

// 上传评论
export async function addComments(comment) {
  console.log({
    "novel": comment.novel_id,
    "chapter": comment.chapter_id,
    "user": comment.user_id,
    "comment_content": comment.content,
    "up_number": comment.up_number,
  });
  try {
    const response = await axios.post('/novels/add_comments', {
      "novel": comment.novel_id,
      "chapter": comment.chapter_id,
      "user": comment.user_id,
      "comment_content": comment.content,
      "up_number": comment.up_number,
    });
    return response.data;
  } catch (error) {
    console.error('Error adding comment:', error);
    return error.code;
  }
}

// 获取评论
export async function getComments(novel_id, chapter_id) {
  console.log({novel_id: novel_id, chapter_id: chapter_id});
  try {
    const response = await axios.get('/novels/get_comments', {
      params: {
        novel_id: novel_id,
        chapter_id: chapter_id
      }
    });
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error('Error fetching comments:', error);
    return error.code;
  }
}

// 注册
export async function register(data) {
  try {
    const response = await axios.post(`/users/register`, {
      "username": data.username,
      "password": data.password,
      "email": data.email,
      "mobile": data.mobile
    });
    return response.data.user_id;
  } catch(error) {
    console.error('Error registering user:', error);
    return error.code;
  }
}