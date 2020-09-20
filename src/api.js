import axios from "axios";

export default {
  // coverPage actions
  covers: () => axios.get("http://127.0.0.1:5000/covers"),
  coverKey: (key, formData) =>
    axios.post(`http://127.0.0.1:5000/covers/${key}`, formData),
  coverPDF: () =>
    axios.get("http://127.0.0.1:5000/covers/pdf", {
      responseType: "arraybuffer",
    }),

  // reviewPage actions
  review: () => axios.get("http://127.0.0.1:5000/review"),

  // toaPage actions
  toaChangeEntry: (IDNumber, formData) =>
    axios.put(`http://127.0.0.1:5000/toa/entries/${IDNumber}/0`, formData),
  insertTOAEntry: (IDNumber, direction) =>
    axios.put(`http://127.0.0.1:5000/toa/entries/${IDNumber}/${direction}`),
  toa: () => axios.get("http://127.0.0.1:5000/toa"),
  removeTOAEntries: () => axios.delete(`http://127.0.0.1:5000/toa/entries`),
  removeTOAEntry: (IDNumber) =>
    axios.delete(`http://127.0.0.1:5000/toa/entries/${IDNumber}`),
  toaPDF: () =>
    axios.get("http://127.0.0.1:5000/toa/pdf", {
      responseType: "arraybuffer",
    }),

  // tocPage actions
  removeTOCEntries: () => axios.delete(`http://127.0.0.1:5000/toc/entries`),
  insertTOCEntry: (IDNumber, direction) =>
    axios.put(`http://127.0.0.1:5000/toc/entries/${IDNumber}/${direction}`),
  removeTOCEntry: (IDNumber) =>
    axios.delete(`http://127.0.0.1:5000/toc/entries/${IDNumber}`),
  tocChangeEntry: (IDNumber, formData) =>
    axios.put(`http://127.0.0.1:5000/toc/entries/${IDNumber}/0`, formData),
  tocPDF: () =>
    axios.get("http://127.0.0.1:5000/toc/pdf", {
      responseType: "arraybuffer",
    }),
  toc: () => axios.get("http://127.0.0.1:5000/toc"),

  // uploadPage actions
  sync: () => axios.get("http://127.0.0.1:5000/sync"),
  reset: () => axios.get("http://127.0.0.1:5000/reset"),
  upload: (formData) => axios.post("http://127.0.0.1:5000/upload", formData),
  removeFile: () => axios.delete(`http://127.0.0.1:5000/upload`),
  cases: (formData) => axios.post("http://127.0.0.1:5000/cases", formData),
  removeCase: (id_number) =>
    axios.delete(`http://127.0.0.1:5000/cases/${id_number}`),
};
