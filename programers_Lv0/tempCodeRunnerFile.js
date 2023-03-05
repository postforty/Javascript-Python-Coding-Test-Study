if (i.length === 1 && i === "x") {
      add += 1;
    } else if (i.length > 1 && i.includes("x")) {
      add += parseInt(i.slice(0, 1));
    }