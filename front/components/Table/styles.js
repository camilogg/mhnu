import styled from 'styled-components'

export const Styles = styled.div`
  /* This is required to make the table full-width */
  display: block;
  max-width: 100%;
  /* box-shadow: 2px 2px 4px hsl(0deg 0% 51% / 16%); */
  box-shadow: 7px 5px 30px rgb(72 73 121 / 15%);
  padding: 2rem;
  background-color: #fff;
  border-radius: 5px;

  /* This will make the table scrollable when it gets too small */
  .tableWrap {
    display: block;
    max-width: 100%;
    overflow-y: hidden;
    border-bottom: 1px solid black;
    ::-webkit-scrollbar {
      height: 10px;
    }
    ::-webkit-scrollbar-track {
      background: #fff; /* color of the tracking area */
    }
    ::-webkit-scrollbar-thumb {
      background-color: #e5e5e5; /* color of the scroll thumb */
      border-radius: 20px; /* roundness of the scroll thumb */
    }
    border: 1px solid #e5e5e5;
  }

  table {
    /* Make sure the inner table is always as wide as needed */
    width: 100%;
    border-spacing: 0;

    tbody tr:nth-of-type(odd) {
      background-color: #f4f5f8;
    }

    tr {
      :last-child {
        td {
          border-bottom: 0;
        }
      }
    }

    th,
    td {
      margin: 0;
      padding: 0.5rem;
      border-bottom: 1px solid #e5e5e5;
      border-right: 1px solid #e5e5e5;
      /* The secret sauce */
      /* Each cell should grow equally */
      width: 1%;
      /* But "collapsed" cells should be as small as possible */
      &.collapse {
        width: 0.0000000001%;
      }

      :last-child {
        border-right: 0;
      }
    }
  }
  .pagination {
    padding: 1rem;

    button {
      width: 40px;
      height: 40px;
      margin: 0 5px;
      display: inline-block;
      background-color: #fff;
      line-height: 40px;
      color: #202647;
      -webkit-box-shadow: 0 2px 10px 0 #d8dde6;
      box-shadow: 0 2px 10px 0 #d8dde6;
      font-size: 15px;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      border-radius: 5px;
      outline: none;
      border: 0;

      :disabled {
        background-color: #eaeaea;
      }
      :hover:enabled {
        color: #fff;
        background-color: #dc3545;
      }
    }
  }
`
