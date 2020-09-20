import { ACTIVATED_FILE } from "./types.js";

export const activateFile = (data) => {
  return {
    type: ACTIVATED_FILE,
    payload: data,
  };
};
